import React from 'react';
import { Button } from 'react-rainbow-components';
import classes from './Elections.module.scss';
import { useNavigate } from 'react-router-dom';

const ElectionCard = ({ type, name, id, isLocal }) => {
  const navigate = useNavigate();

  const handleButtonClick = () => {
    navigate('/election', { state: { id: id } });
  };

  const getType = (type) => {
    switch (type) {
      case 'president':
        return 'prElections.png';
      case 'mayor':
        return 'mElections.png';
      case 'farm':
        return 'fElections.png';
      case 'rector':
        return 'eElections.png';
    }
  };

  return (
    <div className={classes.cardWrapper}>
      <div className={classes.cardName}>
        {isLocal && <img className={classes.iconLocal} src="local.png" style={{height: 80, alignSelf: "center"}} />}
        <img src={getType(type)} style={{width: 80}} />
        <h6>{name}</h6>
      </div>
      <Button
        label="Вибрати ->"
        variant="success"
        className={classes.cardButton}
        onClick={handleButtonClick}
      />
    </div>
  );
};

export default ElectionCard;
