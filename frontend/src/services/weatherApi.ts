// frontend/src/services/weatherApi.ts
import React from 'react';

export interface weatherApiProps {
  className?: string;
}

export const weatherApi: React.FC<weatherApiProps> = (props) => {
  return (
    <div className={props.className}>
      <h3>Create frontend API service client for weather endpoints</h3>
    </div>
  );
};

export default weatherApi;
