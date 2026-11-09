// frontend/src/services/waterApi.ts
import React from 'react';

export interface waterApiProps {
  className?: string;
}

export const waterApi: React.FC<waterApiProps> = (props) => {
  return (
    <div className={props.className}>
      <h3>Create Frontend TypeScript API Client for Water Intake</h3>
    </div>
  );
};

export default waterApi;
