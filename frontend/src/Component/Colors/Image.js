import React from 'react';
import { useSpring, animated } from 'react-spring';


function Image(props) {
    const slideDown = useSpring({from: {marginTop: -500}, to: {marginTop: 0}})
    return (
        <div className="user_image__container" >
            <animated.img className="user_image" src={props.image} style={slideDown} alt="Upload a new image"/>
        </div>
    )
}

export default Image;