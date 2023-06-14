import React, { useState } from 'react';
import classes from './Register.module.scss';
import {
  Input,
  DatePicker,
  Picklist,
  Option,
  Button,
} from 'react-rainbow-components';
import { useNavigate } from 'react-router-dom';

const Register = () => {
  const navigate = useNavigate();

  const inputStyles = {
    width: '300px',
    paddingBottom: 32,
    paddingRight: 15,
    paddingLeft: 15,
    paddingTop: 0,
  };

  const selectStyles = {
    paddingBottom: '32px',
    paddingRight: '15px',
    paddingLeft: '15px',
    width: '300px',
  };

  const [dateState, setDateState] = useState();
  const [locationState, setLocationState] = useState();
  const [emailState, setEmailState] = useState();
  const [passwordState, setPassworState] = useState();
  const [passroetIdState, setPassportIdState] = useState();
  const [nameState, setNameState] = useState();

  const handleRegister = () => {
    const data = {
      email: emailState,
      full_name: nameState,
      password: passwordState,
      passport_id: passroetIdState,
      birthdate: JSON.stringify(dateState).replace(/['"]+/g, ''),
      location: {city: locationState.name},
    };
    console.log('data ----> ', data);
    fetch('http://127.0.0.1:8000/api/voter/register/', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (!response.ok) {
          return response.text().then((text) => {
            throw new Error(text);
          });
        }
        navigate('/login');
        return response.json();
      })
      .catch((error) => {
        console.log(error);
        return Promise.reject();
      });
  };

  return (
    <div className={classes.wrapper}>
      <div className={classes.header}>
        <h1 className={classes.title}>Створення профілю</h1>
        <div className={classes.form}>
          <div className="rainbow-align-content_center rainbow-flex_wrap">
            <Input
              label="Ім'я та прізвище"
              labelAlignment="left"
              placeholder="full name"
              type="text"
              className="rainbow-p-around_medium"
              style={inputStyles}
              onChange={(value) => setNameState(value.target.value)}
            />

            <Input
              label="Електронна пошта"
              labelAlignment="left"
              type="email"
              placeholder="email@example.com"
              className="rainbow-p-around_medium"
              style={inputStyles}
              onChange={(value) => setEmailState(value.target.value)}
            />
          </div>
          <div className="rainbow-align-content_center rainbow-flex_wrap">
            <Input
              label="Пароль"
              labelAlignment="left"
              type="password"
              placeholder="password"
              className="rainbow-p-around_medium"
              style={inputStyles}
              onChange={(value) => setPassworState(value.target.value)}
            />

            <Input
              label="Номер паспорту"
              labelAlignment="left"
              placeholder="passport ID"
              type="text"
              className="rainbow-p-around_medium"
              style={inputStyles}
              onChange={(value) => setPassportIdState(value.target.value)}
            />
          </div>
          <div className="rainbow-align-content_center rainbow-flex_wrap">
            <Picklist
              id="picklist-1"
              labelAlignment="left"
              style={selectStyles}
              onChange={(value) => setLocationState(value)}
              value={locationState}
              label="Регіон"
            >
              <Option
                name="header"
                label="Available locations"
                variant="header"
              />
              <Option name="Cherkasy" label="Cherkasy" />
              <Option name="Chernihiv" label="Chernihiv" />
              <Option name="Chernivtsi" label="Chernivtsi" />
              <Option name="Dnipro" label="Dnipro" />
              <Option name="Dnipro" label="Dnipro" />
              <Option name="Ivano-Frankivsk" label="Ivano-Frankivsk" />
              <Option name="Kharkiv" label="Kharkiv" />
              <Option name="Kherson" label="Kherson" />
              <Option name="Khmelnytsk" label="Khmelnytsk" />
              <Option name="Kropyvnytskyi" label="Kropyvnytskyi" />
              <Option name="Kyiv" label="Kyiv" />
              <Option name="Luhansk" label="Luhansk" />
              <Option name="Lviv" label="Lviv" />
              <Option name="Odesa" label="Odesa" />
              <Option name="Poltava" label="Poltava" />
              <Option name="Rivne" label="Rivne" />
              <Option name="Sumy" label="Sumy" />
              <Option name="Ternopil" label="Ternopil" />
              <Option name="Vinnytsya" label="Vinnytsya" />
              <Option name="Lutsk" label="Lutsk" />
              <Option name="Uzhgorod" label="Uzhgorod" />
              <Option name="Zaporizhzhya" label="Zaporizhzhya" />
              <Option name="Zhytomyr" label="Zhytomyr" />
            </Picklist>
            <DatePicker
              value={dateState}
              labelAlignment="left"
              placeholder="дд/мм/рррр"
              minDate={new Date(1950, 1, 1)}
              maxDate={new Date(2004, 1, 1)}
              label="Дата народження"
              onChange={(value) => setDateState(value)}
              style={selectStyles}
              className={classes.reactRainbowDatepicker_container}
              variant="double"
            />
          </div>
        </div>
        <Button
          label="Реєстрація"
          variant="success"
          className={classes.button}
          onClick={handleRegister}
        />

      </div>
    </div>
  );
};

export default Register;
