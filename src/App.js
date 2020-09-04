import React, { useState, useEffect } from 'react'
import Moment from 'react-moment'
import { CardStack, Card } from 'react-cardstack'

import './App.css'

class Card2 extends React.Component {
     handleCardClick(isCardSelected) {
  	     console.log(isCardSelected);
     }

     render() {
         return <Card key="{this.props.id}" background='#29C0B9' cardClicked={this.handleCardClick.bind(this)}>
            <h1>{this.props.title}</h1>
            <p>{this.props.content}</p>
            </Card>
    }
}

function deck(cards){
    let dk = cards.map( (props) => {
        return ( <Card key={props.id} background='#29C0B9'>
          <h1>{props.title}</h1>
          <p>{props.content}</p>
        </Card> )
    })
    return dk
}

const palette = ['#F8B195', '#F67280', '#C06C84', '#6C5B7B', '#355C7D']
function card(props, idx){
    return ( <Card key={props.id} background={palette[idx]}>
      <h1>{props.title}</h1>
      <p>{props.content}</p>
    </Card> )
}

function App() {
  const [currentTime, setCurrentTime] = useState(0)
  const [currentPosts, setCurrentPosts] = useState([])
  // const [currentPosts, setCurrentPosts] = useState([{id:'10',title:'State',content:''},{id:'11',title:'Loading',content:''}])

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
      <Moment unix date={currentTime}/>
      <CardStack height={500} width={400} background={palette[4]} hoverOffset={25}>
      {currentPosts.length === 0 ? <Card key="999" background={palette[0]}><h1>Posts</h1></Card> : <span/> }
      {currentPosts.length === 0 ? <Card key="998" background={palette[1]}><h1>Loading...</h1></Card> : <span/> }
      {currentPosts.length > 0 ? card(currentPosts[0], 0) : <span/> }
      {currentPosts.length > 1 ? card(currentPosts[1], 1) : <span/> }
      {currentPosts.length > 2 ? card(currentPosts[2], 2) : <span/> }
      {currentPosts.length > 3 ? card(currentPosts[3], 3) : <span/> }
      {currentPosts.length > 4 ? card(currentPosts[4], 4) : <span/> }
      </CardStack>
      </header>
    </div>
  );
}

export default App;
