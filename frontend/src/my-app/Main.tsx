import * as React from 'react'

// 1. import `ChakraProvider` component
import { ChakraProvider } from '@chakra-ui/react'
import MainPage from './MainPage';

const Main= () => {
    return (
        <ChakraProvider>
            <MainPage />
        </ChakraProvider>
    );
}

export default Main;