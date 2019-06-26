import React from 'react';
import lightOrDark from'./Helper';
import { Spring } from 'react-spring/renderprops';


function blackOrWhite(color) {
  const hue = lightOrDark(color)

  if (hue === 'light') {
    return '#000000'
  } else {
    return '#ffffff'
  }
}


function ColorPalette(props) {
    const name = "color_box";
    const colors = props.colors;
    let delay = 50;

    const colorBoxes = colors.map((color) => {
        let fontColor = blackOrWhite(color)
        delay += 50
        return (
          <Spring
          from={{opacity: 0}}
          to={{opacity: 1, backgroundColor: color}}
          delay={delay.toString()}
          >

          {props => (
            <div className={name} style={props}>
              <div className="color_box__labels" style={{color: fontColor}}>{color}</div>
            </div>
          )
          }
          </Spring>
        )
      }
    )
    return (
      <div className="color_box__container">
        {colorBoxes}
      </div>
    )
  }

  export default ColorPalette;