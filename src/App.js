import React, { useState, useEffect } from 'react'
import { CardStack, Card } from 'react-cardstack'

import './App.css'

function App() {
  const [currentTime, setCurrentTime] = useState(0)
  const [currentPosts, setCurrentPosts] = useState([])

  useEffect(() => {
    fetch('/time')
        .then(res => res.json())
        .then(data => setCurrentTime(data.time))
  }, [])

  useEffect(() => {
    fetch('/posts')
        .then(res => res.json())
        .then(data => setCurrentPosts(data.posts))
  }, [])

  return (
    <div className="App">
      <header className="App-header">
      <p>The current time is {currentTime}.</p>
      <CardStack height={500} width={400} background='#f8f8f8' hoverOffset={25}>
      <Card key="1" background='#29C0B9'>
        <h1>{currentPosts.length ? currentPosts[0].title : 'Loading...'}</h1>
        <p>{currentPosts.length ? currentPosts[0].content : null}</p>
      </Card>
      <Card key="2" background='#2930B9'>
      <h1>{currentPosts.length ? currentPosts[1].title : 'Loading...'}</h1>
      <p>{currentPosts.length ? currentPosts[1].content : null}</p>
      </Card>
      </CardStack>
      </header>
    </div>
  );
}

export default App;
