import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route, Navigate, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import Pull from './pages/pull';
import Home from './pages/home';
import Show from './pages/show';
import Login from './pages/login';
import ShowST from './pages/showst';
import ShowLD from './pages/showld';
import PullST from './pages/pullst';
import PullLD from './pages/pullld';
import ShowDis from './pages/showdis';
import PullSuc from './pages/pullsuccess';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem("token"));

  useEffect(() => {
    const checkAuth = () => setIsAuthenticated(!!localStorage.getItem("token"));
    window.addEventListener("storage", checkAuth); // ✅ ฟัง event localStorage เปลี่ยนค่า
    return () => window.removeEventListener("storage", checkAuth);
  }, []);

  function LayoutWithNavbar({ children }) {
    const location = useLocation();
    const showNavbar = isAuthenticated && location.pathname !== "/";
    return (
      <>
        {showNavbar && <Navbar setIsAuthenticated={setIsAuthenticated} />}
        {children}
      </>
    );
  }

  return (
    <div className="Container">
      <Router>
        <LayoutWithNavbar>
          <Routes>
            <Route path="/" element={isAuthenticated ? <Navigate to="/home" replace /> : <Login setIsAuthenticated={setIsAuthenticated} />} />
            <Route path="/home" element={isAuthenticated ? <Home /> : <Navigate to="/" replace />} />
            <Route path="/pull" element={isAuthenticated ? <Pull /> : <Navigate to="/" replace />} />
            <Route path="/show" element={isAuthenticated ? <Show /> : <Navigate to="/" replace />} />
            <Route path="/showst" element={isAuthenticated ? <ShowST /> : <Navigate to="/" replace />} />
            <Route path="/showld" element={isAuthenticated ? <ShowLD /> : <Navigate to="/" replace />} />
            <Route path="/pullst" element={isAuthenticated ? <PullST /> : <Navigate to="/" replace />} />
            <Route path="/pullld" element={isAuthenticated ? <PullLD /> : <Navigate to="/" replace />} />
            <Route path="/showdis" element={isAuthenticated ? <ShowDis /> : <Navigate to="/" replace />} />
            <Route path="/pullsuccess" element={isAuthenticated ? <PullSuc /> : <Navigate to="/" replace />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </LayoutWithNavbar>
      </Router>
    </div>
  );
}

export default App;
