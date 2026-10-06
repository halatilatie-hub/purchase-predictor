import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [status, setStatus] = useState('Checking backend connection...')
  const [error, setError] = useState('')

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

  return (
    <main className="connection-status">
      <h1>Connection status</h1>
      <p>{status}</p>
      {error && <p className="error">Error: {error}</p>}
      <p>Frontend is pointing to http://localhost:8080</p>
    </main>
  )
}

export default App
