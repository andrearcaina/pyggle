'use client';
import { useState, useEffect } from 'react';

export default function Home() {
  const [allWords, setAllWords] = useState([]);

  useEffect(() => {
    fetchWords();
  }, []);
  
  const fetchWords = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/words/ae st&words=3000&official=True")
      const data = await response.json();
      setAllWords(data);
    } catch (error) {
      console.error("Error fetching FastAPI response:, ", error);
    }
  }

  return (
    <main>
      {allWords.map((word, index) => (
        <div key={index}>
          <p> {word} </p>
        </div>
      ))}
    </main>
  );
}
