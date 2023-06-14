import React, { useState, useEffect, useContext } from 'react';
import CandidateCard from './CandidateCard';
import classes from './Candidates.module.scss';
import { useLocation } from 'react-router-dom';
import AuthContext from '../../context/AuthProvider';

const Candidates = () => {
  const location = useLocation();
  const electionId = location.state.id;
  const [election, setElection] = useState();
  const [myVote, setMyVote] = useState();
  const isElectionFlexible = election?.is_flexible;
  const { auth } = useContext(AuthContext);

  const getMyVote = () => {
    fetch(
      `http://127.0.0.1:8000/api/election/details/${userId}/${electionId}`,
      {
        method: 'GET',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        },
      }
    )
      .then((response) => {
        if (!response.ok) {
          return response.text().then((text) => {
            throw new Error(text);
          });
        }
        return response.json();
      })
      .then((responseJson) => {
        setMyVote(responseJson);
        console.log(responseJson, 'vote');
      })
      .catch((error) => {
        console.log(error);
        return Promise.reject();
      });
  };

  function getCookie(name) {
    var nameEQ = name + '=';
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) === ' ') c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
  }
  const userId = getCookie('passportId');

  useEffect(() => {
    getMyVote();
    fetch(`http://127.0.0.1:8000/api/electionById/${electionId}`, {
      method: 'GET',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    })
      .then((response) => {
        if (!response.ok) {
          return response.text().then((text) => {
            throw new Error(text);
          });
        }
        return response.json();
      })
      .then((responseJson) => {
        setElection(responseJson);
        console.log(responseJson);
      })
      .catch((error) => {
        console.log(error);
        return Promise.reject();
      });
  }, []);

  return (
    <div className={classes.wrapper}>
      <div className={classes.header}>
        <h1 className={classes.title}>
          Проголосуйте
        </h1>
        {election?.candidates && (
          <div className={classes.grid}>
            {election.candidates.map(
              ({ full_name, description, id, image_url }) => (
                <CandidateCard
                  key={`${id}`}
                  name={full_name}
                  description={description}
                  imgUrl={image_url}
                  electionId={electionId}
                  userId={auth}
                  candidateId={id}
                  isSelected={myVote?.id === id}
                  isDisabled={
                    !!myVote?.id ? (myVote?.id !== id) : false
                  }
                  isFlexible={isElectionFlexible}
                />
              )
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default Candidates;
