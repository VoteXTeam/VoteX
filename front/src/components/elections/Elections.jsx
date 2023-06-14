import React, { useEffect, useState, useContext } from 'react';
import PermissionDenied from '../permissionDenied/PermissionDenied';
import ElectionCard from './ElectionCard';
import classes from './Elections.module.scss';
import AuthContext from '../../context/AuthProvider';

const Elections = () => {
  const [electionsData, setElectionsData] = useState(null);

  const { auth } = useContext(AuthContext);

  const isLoggedIn = !!auth;

  const electionTypes = ['president', 'mayor', 'farm', 'rector'];


  useEffect(() => {
    if (auth) {
      fetch(`http://127.0.0.1:8000/api/elections/${auth}`, {
        method: 'GET',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error(response.statusText);
          }
          return response.json();
        })
        .then((responseJson) => {
          setElectionsData(responseJson);

        })
        .catch((error) => {
          console.log(error);
        });

    }
  }, [auth]);


  return (
    <>
      {isLoggedIn ? (
        <div className={classes.wrapper}>
          <div className={classes.header}>
            <h1 className={classes.title}>Виберіть вибори</h1>
            {electionsData && (
              <div className={classes.grid}>

                {electionsData.map((election, index) => (
                  <ElectionCard
                    key={election.id}
                    name={election.name}
                    id={election.id}
                    type={electionTypes[`${index > 3 ? index % 4 : index}`]}
                    isLocal={election?.location}
                  />
                ))}
              </div>
            )}
          </div>
        </div>
      ) : (
        <PermissionDenied />
      )}
    </>
  );
};

export default Elections;
