// frontend/src/components/NotesApp.tsx
import React from 'react';

export interface NotesAppProps {
  className?: string;
}

export const NotesApp: React.FC<NotesAppProps> = (props) => {
  return (
    <div className={props.className}>
      <h3>Create React Notes UI Component</h3>
    </div>
  );
};

export default NotesApp;
