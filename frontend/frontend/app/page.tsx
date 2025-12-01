"use client";
import { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";

export interface AgentResponse {
  symptom: string;
  analysis: string;
  home_remedy: string;
  emergency_guideline: string;
  memory: string[];
  quality_report: {
    is_valid: boolean;
    issues: string[];
  };
}




export default function Home() {

  function formatResponse(data: AgentResponse) {
  return `
  **🩺 Symptom:** ${data.symptom}

  **📊 Analysis:**  
  ${data.analysis}

  **🏡 Home Remedy:**  
  ${data.home_remedy}

  **🚨 Emergency Guideline:**  
  ${data.emergency_guideline}

  **🧠 Memory Used:**  
  ${data.memory.join(", ")}

  **✔ Quality Check:** ${data.quality_report.is_valid ? "Valid" : "Issues detected"}
  `;
  }


  const [messages, setMessages] = useState<{ role: string; content: string }[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  


  // Send Message
const sendMessage = async () => {
  if (!input.trim()) return;

  const userMessage = { role: "user", content: input };
  setMessages((m) => [...m, userMessage]);
  setInput("");
  setLoading(true);

  try {
    const res = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ symptom: userMessage.content }),
    });

    const data = await res.json();
    const typed: AgentResponse = data;

    

    // If backend returns directly the agent result
    const botMessage = {
  role: "assistant",
  content: formatResponse(typed),
};



    setMessages((m) => [...m, botMessage]);
  } catch (error) {
    setMessages((m) => [
      ...m,
      { role: "assistant", content: "⚠️ Server Offline or Error Occurred" },
    ]);
  }

  setLoading(false);
};


  // Allow Enter key to send message
  const handleKey = (e: any) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <div className="w-64 bg-white shadow-xl p-5 border-r">
        <h1 className="text-2xl font-bold mb-4">HealthGuard-AI</h1>
        <p className="text-sm text-gray-600">
          A medical triage agent powered by AI + MCP tools.  
          Ask anything about symptoms, diagnosis, or first aid.
        </p>
      </div>

      {/* Chat Window */}
      <div className="flex flex-col flex-1">
        {/* Messages */}
        <div className="flex-1 overflow-y-auto p-6 space-y-4">
          {messages.map((msg, idx) => (
            <div
              key={idx}
              className={`p-3 rounded-xl max-w-xl ${
                msg.role === "user"
                  ? "bg-blue-500 text-white ml-auto"
                  : "bg-white shadow"
              }`}
            >
              <ReactMarkdown>{msg.content}</ReactMarkdown>

            </div>
          ))}
          {loading && (
            <div className="p-3 rounded-xl bg-white shadow w-32">
              <span className="animate-pulse">Thinking…</span>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Bar */}
        <div className="p-4 bg-white border-t flex gap-2">
          <input
            className="flex-1 p-3 border rounded-xl focus:ring focus:ring-blue-300"
            placeholder="Type your symptoms..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKey}
          />
          <button
            onClick={sendMessage}
            className="px-5 py-3 bg-blue-600 text-white rounded-xl hover:bg-blue-700"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
