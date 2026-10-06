import { useEffect, useState } from 'react'
import { checkBackendHealth } from '../services/api'

export function useReceipts() {
  const [status, setStatus] = useState('Checking backend connection...')
  const [error, setError] = useState('')

  useEffect(() => {
    checkBackendHealth()
      .then((data) => {
        setStatus(data.status === 'ok' ? 'Backend connected successfully' : 'Backend responded')
      })
      .catch((err) => {
        setStatus('Backend connection failed')
        setError(err.message)
      })
  }, [])

  return { status, error }
}
