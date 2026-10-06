import ReceiptUpload from '../components/ReceiptUpload'

export default function HomePage() {
  return (
    <main className="page">
      <h1>Purchase Predictor</h1>
      <p>Upload a receipt and track purchasing trends over time.</p>
      <ReceiptUpload />
    </main>
  )
}
