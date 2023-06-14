import React, { useContext } from 'react';
import classes from './Footer.module.scss';
import { useNavigate, useLocation } from 'react-router-dom';
import { Button } from 'react-rainbow-components';
import AuthContext from '../../context/AuthProvider';

const Footer = () => {
  const { auth } = useContext(AuthContext);

  const navigate = useNavigate();
  const location = useLocation();

  const isFooter =
    location.pathname !== '/register' && location.pathname !== '/login' && auth;

  const getLabel = () => {
    if (location.pathname === '/elections' || location.pathname === '/election')
      return 'Статистика';
    else if (location.pathname === '/statistics') return 'Вибори';
  };

  const handleClick = () => {
    if (location.pathname === '/elections' || location.pathname === '/election')
      navigate('/statistics');
    else if (location.pathname === '/statistics') navigate('/elections');
  };

  return (
    <>
      {isFooter && (
        <div className={classes.wrapper}>
          <Button
            onClick={handleClick}
            variant="success"
            className={classes.button}
          >
            {getLabel()}
            <img src="statistics.png" />
          </Button>
        </div>
      )}
    </>
  );
};

export default Footer;
