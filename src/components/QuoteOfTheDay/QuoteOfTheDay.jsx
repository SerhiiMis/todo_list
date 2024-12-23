import { useEffect, useState } from "react";

const QuoteOfTheDay = () => {
  const [quote, setQuote] = useState("");
  const [author, setAuthor] = useState("");
  const [laoding, setLoading] = useState(true);

  useEffect(() => {
    const fetchQuote = async () => {
      try {
        const response = await fetch(
          "https://your-energy.b.goit.study/api/quote"
        );
        const data = await response.json();
        setQuote(data.quote);
        setAuthor(data.author);
      } catch (error) {
        console.error("Error fetching quote:", error);
        setQuote("Keep pushing forward!");
        setAuthor("Unknown");
      } finally {
        setLoading(false);
      }
    };

    fetchQuote();
  }, []);

  return (
    <div>
      <h2>Quote of the Day</h2>
      {laoding ? (
        <p>Loading...</p>
      ) : (
        <blockquote>
          <p>{quote}</p>
          <p>
            <strong>{author}</strong>
          </p>
        </blockquote>
      )}
    </div>
  );
};

export default QuoteOfTheDay;
