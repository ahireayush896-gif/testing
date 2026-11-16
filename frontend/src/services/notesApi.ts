// frontend/src/services/notesApi.ts
import React from 'react';

export interface notesApiProps {
  className?: string;
}

export const notesApi: React.FC<notesApiProps> = (props) => {
  return (
    <div className={props.className}>
      <h3>Create Frontend TypeScript API Client for Notes</h3>
    </div>
  );
};

export default notesApi;
