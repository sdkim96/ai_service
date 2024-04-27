import { Box } from "@chakra-ui/react";

const MainPage = () => {

    const data: string = "33";
    console.log(data);

    return (
        <Box bg='orange'>
            <h1>My App</h1>
            <p>Welcome to my app!</p>
        </Box>
    );
};

export default MainPage;