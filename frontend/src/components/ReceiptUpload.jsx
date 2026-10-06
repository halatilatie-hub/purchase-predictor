export default function ReceiptUpload() {
  return (
    <section className="card">
      <h2>Upload receipt</h2>
      <input type="file" accept="image/*" />
      <button type="button">Analyze receipt</button>
    </section>
  )
}
