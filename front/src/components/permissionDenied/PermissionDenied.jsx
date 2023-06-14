import React from 'react';
import { Button } from 'react-rainbow-components';
import classes from './PermissionDenied.module.scss';
import { useNavigate } from 'react-router-dom';

const PermissionDenied = () => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate('/register');
  };

  return (
    <div className={classes.wrapper}>
      <div className={classes.header}>
        <h1 className={classes.title}>Виберіть вибори</h1>
        <div className={classes.permissionCard}>
          <div className={classes.infoSection}>
            <img src="denied.png" style={{width: 80}}/>
            <div className={classes.text}>
              <h5>В Дозволі відмовлено</h5>
              <h6>Для перегляду цієї сторінки вам потрібно створити обліковий запис</h6>
            </div>
          </div>
          <Button
              variant="success"
            label="Створити новий"
            onClick={handleClick}
            className={classes.button}
          />
        </div>
      </div>
    </div>
  );
};

export default PermissionDenied;
