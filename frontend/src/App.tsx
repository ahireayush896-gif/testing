// frontend/src/App.tsx
import React from 'react';
import FinanceAdvisor from './frontend/src/components/FinanceAdvisor';


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
