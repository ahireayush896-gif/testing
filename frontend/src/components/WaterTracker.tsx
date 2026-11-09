// frontend/src/components/WaterTracker.tsx
import React from 'react';

export interface WaterTrackerProps {
  className?: string;
}

export const WaterTracker: React.FC<WaterTrackerProps> = (props) => {
  return (
    <div className={props.className}>
      <h3>Build React Water Intake Dashboard and Component</h3>
    </div>
  );
};

export default WaterTracker;
