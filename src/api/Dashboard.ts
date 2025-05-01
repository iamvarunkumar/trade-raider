import { useEffect, useState } from "react";
import { fetchSuggestions } from "../api/suggestions";

type Suggestion = { symbol: string; category: string };

export function Dashboard() {
  const [data, setData] = useState<Suggestion[]>([]);

  useEffect(() => {
    fetchSuggestions().then(setData);
  }, []);

  return (
    <main className="p-6">
      <h1 className="text-2xl font-bold mb-4">Top 10 Suggestions (Stub)</h1>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {data.map((s) => (
          <div
            key={s.symbol}
            className="border rounded p-4 shadow flex flex-col items-center"
          >
            <span className="text-lg font-semibold">{s.symbol}</span>
            <span className="text-sm text-gray-500">{s.category}</span>
          </div>
        ))}
      </div>
    </main>
  );
}
