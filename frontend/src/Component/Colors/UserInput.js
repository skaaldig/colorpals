import React from 'react';

function UserInput(props) {
    return (
      <div className="upload_bar__container">
        <div className="upload_bar__item">
          <input type="file" id="file" accept="image/png, image/jpeg" onChange={props.onChange} />
          <label for="file">Choose a File</label>
        </div>
        <div className="upload_bar__item">
          <button className="bttn" onClick={props.onClick}>Upload</button>
        </div>
      </div>
    )
  }

  export default UserInput;