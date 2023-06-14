import { BrowserRouter } from 'react-router-dom';
import Header from './components/header/Header';
import Footer from './components/footer/Footer';
import AppRoutes from './config/Routes';
import { Application } from 'react-rainbow-components';
import { AuthProvider } from './context/AuthProvider';

function App() {
  return (
    <Application>
      <AuthProvider>
        <BrowserRouter>
          <Header />
          <AppRoutes />
          <Footer />
        </BrowserRouter>
      </AuthProvider>
    </Application>
  );
}

export default App;
