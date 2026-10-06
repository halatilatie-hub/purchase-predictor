import { useEffect, useRef, useState } from 'react'
import './App.css'

const MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024
const ALLOWED_FILE_TYPES = new Set(['image/jpeg', 'image/png', 'image/webp'])
const ALLOWED_FILE_EXTENSIONS = new Set(['.jpg', '.jpeg', '.png', '.webp'])

function App() {
  const [status, setStatus] = useState('Checking backend connection...')
  const [error, setError] = useState('')
  const [selectedFile, setSelectedFile] = useState(null)
  const [previewUrl, setPreviewUrl] = useState('')
  const [uploading, setUploading] = useState(false)
  const [uploadedFile, setUploadedFile] = useState(null)
  const fileInputRef = useRef(null)

  useEffect(() => {
    fetch('http://localhost:8080/health')
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`)
        }
        return response.json()
      })
      .then((data) => {
        setStatus(data.status === 'ok' ? 'Backend connected successfully' : 'Backend responded')
      })
      .catch((err) => {
        setStatus('Backend connection failed')
        setError(err.message)
      })
  }, [])

  useEffect(() => {
    return () => {
      if (previewUrl) {
        URL.revokeObjectURL(previewUrl)
      }
    }
  }, [previewUrl])

  const handleFileChange = (event) => {
    const file = event.target.files?.[0]

    if (!file) {
      setSelectedFile(null)
      setPreviewUrl('')
      return
    }

    const fileExtension = file.name ? file.name.substring(file.name.lastIndexOf('.')).toLowerCase() : ''
    const isAllowedType = ALLOWED_FILE_TYPES.has(file.type) || file.type.startsWith('image/')
    const isAllowedExtension = ALLOWED_FILE_EXTENSIONS.has(fileExtension)

    if (!isAllowedType || !isAllowedExtension) {
      setError('Invalid file type. Please upload a JPG, JPEG, PNG, or WEBP image.')
      setSelectedFile(null)
      setPreviewUrl('')
      return
    }

    if (file.size > MAX_FILE_SIZE_BYTES) {
      setError('File exceeds the 10 MB limit. Please upload an image smaller than 10 MB.')
      setSelectedFile(null)
      setPreviewUrl('')
      return
    }

    setError('')
    setSelectedFile(file)
    setPreviewUrl(URL.createObjectURL(file))
  }

  const handleUpload = async () => {
    if (!selectedFile) {
      setError('Please choose a receipt image first.')
      return
    }

    if (!ALLOWED_FILE_TYPES.has(selectedFile.type) && !selectedFile.type.startsWith('image/')) {
      setError('Invalid file type. Please upload a JPG, JPEG, PNG, or WEBP image.')
      return
    }

    if (selectedFile.size > MAX_FILE_SIZE_BYTES) {
      setError('File exceeds the 10 MB limit. Please upload an image smaller than 10 MB.')
      return
    }

    setUploading(true)
    setError('')

    const formData = new FormData()
    formData.append('file', selectedFile)

    try {
      const response = await fetch('http://localhost:8080/upload-receipt', {
        method: 'POST',
        body: formData,
      })

      const data = await response.json().catch(() => ({}))

      if (!response.ok) {
        throw new Error(data.detail || 'Upload failed. Please try again.')
      }

      setUploadedFile(data)
      setStatus('Receipt uploaded successfully')
      setSelectedFile(null)
      setPreviewUrl('')

      if (fileInputRef.current) {
        fileInputRef.current.value = ''
      }
    } catch (err) {
      setError(err.message)
      setStatus('Receipt upload failed')
    } finally {
      setUploading(false)
    }
  }

  return (
    <main className="connection-status">
      <h1>Receipt upload</h1>
      <p>{status}</p>
      {error && <p className="error">Error: {error}</p>}

      <div className="upload-card">
        <label htmlFor="receipt-upload" className="upload-label">
          Choose a receipt image
        </label>
        <input
          id="receipt-upload"
          ref={fileInputRef}
          type="file"
          accept="image/png,image/jpeg,image/webp"
          onChange={handleFileChange}
        />

        {previewUrl && (
          <img src={previewUrl} alt="Selected receipt preview" className="preview-image" />
        )}

        {selectedFile && <p className="file-name">Selected file: {selectedFile.name}</p>}

        <button type="button" onClick={handleUpload} disabled={!selectedFile || uploading}>
          {uploading ? 'Uploading...' : 'Upload receipt'}
        </button>
      </div>

      {uploadedFile && (
        <div className="upload-result">
          <h2>Upload result</h2>
          <p>
            <strong>Filename:</strong> {uploadedFile.filename}
          </p>
          <p>
            <strong>Saved file:</strong> {uploadedFile.saved_filename}
          </p>
          <p>
            <strong>Size:</strong> {uploadedFile.size} bytes
          </p>
          <p>
            <strong>Status:</strong> {uploadedFile.status}
          </p>
        </div>
      )}

      <p>Frontend is pointing to http://localhost:8080</p>
    </main>
  )
}

export default App
