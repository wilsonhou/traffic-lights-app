import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [jsonData, setJsonData] = useState("");
  useEffect(() => {
    fetch("../../syllabus-script/end-data/chemistry-stage6-syllabus-pdf.json", {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
      }
    })
      .then(response => {
        if (response.ok) {
          return response.json();
        }
      })
      .then(data => {
        console.log(data);
        setJsonData(data);
      });
  });
  return <div className="App">{jsonData}</div>;
}

export default App;
