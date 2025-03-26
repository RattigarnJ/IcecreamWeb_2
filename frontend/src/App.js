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
import PullSuc from './pages/pullsuccess'

function App() {

  return (
    <div className="Containner">
      <Router>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/*" element={
            <>
              <Navbar />
              <Routes>
                <Route path="/home" element={<Home />} />
                <Route path="/pull" element={<Pull />} />
                <Route path="/show" element={<Show />} />
                <Route path="/showst" element={<ShowST />} />
                <Route path="/showld" element={<ShowLD />} />
                <Route path="/pullst" element={<PullST />} />
                <Route path="/pullld" element={<PullLD />} />
                <Route path="/showdis" element={<ShowDis />} />
                <Route path="/pullsuccess" element={<PullSuc />} />
              </Routes>
            </>
          } />
        </Routes>
        </Router>
    </div>
  );
}

export default App;
