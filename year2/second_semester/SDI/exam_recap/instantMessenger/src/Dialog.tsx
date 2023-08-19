import React, { useState } from "react";

type DialogProps = {
  onClose: () => void;
  onSave: (value: string) => void;
};
const Dialog: React.FC<DialogProps> = ({ onClose, onSave }) => {
  const [inputValue, setInputValue] = useState("");
  const [error, setError] = useState<string>("");

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
  };

  const handleSave = (e: { preventDefault: () => void }) => {
    e.preventDefault();
    if (inputValue.trim() === "") {
      setError("Input cannot be empty");
      return;
    }
    onSave(inputValue);
  };

  const handleCancel = () => {
    setInputValue("");
    onClose();
  };
  return (
    <div className="dialog-overlay">
      <div className="dialog">
        <h2>Create Channel</h2>
        <p> enter channel name:</p>
        <input type="text" value={inputValue} onChange={handleInputChange} />
        {error !== "" && <p>{error}</p>}
        <button onClick={handleSave}>Save</button>
        <button onClick={handleCancel}>Cancel</button>
      </div>
    </div>
  );
};

export default Dialog;
