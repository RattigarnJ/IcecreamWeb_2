import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Pull from './pages/pull'
import Home from './pages/home'
import Show from './pages/show'
import Login from './pages/login'
import ShowST from './pages/showst'
import ShowLD from './pages/showld'
import PullST from './pages/pullst'
import PullLD from './pages/pullld'
import ShowDis from './pages/showdis'

function App() {

  return (
    <div className="Containner">
      <Router>
      <Navbar />
      <div style={{ paddingTop: "60px" }}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/pull" element={<Pull />} />
        <Route path="/show" element={<Show />} />
        <Route path="/login" element={<Login />} />
        <Route path='/showst' element={<ShowST />} />
        <Route path='/showld' element={<ShowLD />} />
        <Route path='/pullst' element={<PullST />} />
        <Route path='/pullld' element={<PullLD />} />
        <Route path='/showdis' element={<ShowDis />} />
      </Routes>
      </div>
      </Router>
    </div>
  );
}

export default App;
