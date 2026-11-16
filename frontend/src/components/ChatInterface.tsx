// frontend/src/components/ChatInterface.tsx
import React from 'react';

export interface ChatInterfaceProps {
  className?: string;
}

export const ChatInterface: React.FC<ChatInterfaceProps> = (props) => {
  return (
    <div className={props.className}>
      <h3>Create React ChatInterface Component</h3>
    </div>
  );
};

export default ChatInterface;
