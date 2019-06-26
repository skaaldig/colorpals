import React, { Component } from "react";
import UserInput from './UserInput';
import ColorPalette from './ColorPalette';
import Instructions from './Instructions';
import Image from './Image';

import axios from "axios";

function makeHexArray(hexObject) {
  const hexArray = Object.values(hexObject).slice(1,11)
  return hexArray
}


export default class Colors extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedFile: null,
      uploadedImage: null,
      colors: Array(10).fill(1).map(x => "#ffffff"),
    }

    this.fileSelectedHandler = this.fileSelectedHandler.bind(this);
    this.fileUploadHandler = this.fileUploadHandler.bind(this);
  }

  fileSelectedHandler(event) {
    this.setState({selectedFile: event.target.files[0]})
  }

  fileUploadHandler() {
    const fd = new FormData();
    fd.append('image', this.state.selectedFile, this.state.selectedFile.name)
    axios.post('http://localhost:8000/api/images/', fd)
      .then(res => {
        this.setState({uploadedImage: res.data.image})
        this.setState({colors: makeHexArray(res.data.top_colors)})
      })
  }

  render() {
    const hasColors = this.state.colors
    let colors
    if (hasColors) {
      colors = <ColorPalette colors={this.state.colors}/>
    } else {
      colors = null
    }

    const imageUploaded = this.state.uploadedImage
    let image
    if (imageUploaded) {
      image = <Image image={this.state.uploadedImage} />
    } else {
      image = <Instructions />
    }

    return(
      <div className="app__container">
        {image}
        <UserInput onChange={this.fileSelectedHandler} onClick={this.fileUploadHandler} />
        {colors}
      </div>
    )
  }
}