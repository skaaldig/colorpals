import React from 'react';
import { useSpring, animated } from 'react-spring';


function Instructions(props) {
    const slideIn = useSpring({from: {marginLeft: -700}, to: {marginLeft: 0}})
    return (
    <div className="instructions">
        <animated.div className="instructions__wrapper" style={slideIn}>
            <h1 className="instructions__h1">
                10 Most Prevalent Colors
            </h1>
            <p className="lead">
                Upload a photo to discover the 10 most prevalent colors in the image and their hexidecimal codes.
            </p>
        </animated.div>
    </div>
    )
}

export default Instructions;