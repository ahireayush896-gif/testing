// frontend/src/services/authApi.ts
import React from 'react';

export interface authApiProps {
  className?: string;
}

export const authApi: React.FC<authApiProps> = (props) => {
  return (
    <div className={props.className}>
      <h3>Create Frontend API Service for User Profile</h3>
    </div>
  );
};

export default authApi;
