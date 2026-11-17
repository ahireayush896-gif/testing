// frontend/src/App.tsx
import React from 'react';
import BeeDetector from './frontend/src/components/BeeDetector';


export interface AppProps {
  className?: string;
}

export const App: React.FC<AppProps> = (props) => {
  return (
    <div className={props.className}>
      <h3>Integrate Notes Component into Frontend Entrypoint</h3>
    </div>
  );
};

export default App;
