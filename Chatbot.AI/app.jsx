import ChatInterface from './ChatInterface'

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h1 className="text-3xl font-bold text-center mb-8">AI Chatbot</h1>
      <div className="max-w-4xl mx-auto">
        <ChatInterface />
      </div>
    </div>
  )
}

export default App