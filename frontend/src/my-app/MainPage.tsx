import {
    Box, Container, Table, Thead, Tbody, Tfoot, 
    Tr, Th, Td, TableCaption, TableContainer, } from "@chakra-ui/react";
import { useEffect, useState } from "react";

const MainPage = () => {

    interface Message {
        id: string;
        content:[{
            text: {
                value: string;
            }
        }];
    };
    
    const [openaiMessage, setOpenaiMessage] = useState<Message[]>([]);


    const getOpenaiMessages = async () => {
        const response = await fetch('http://localhost:8000/fastapi/openai/get_messages?thread_id=thread_h2A5dGWSHD26lIldYzE51Ywt');
        const data = await response.json();
        setOpenaiMessage(data);
    }

    

    useEffect(()=>{
        getOpenaiMessages();
    }, [])



    return (
        <Container maxW='80%'>
            <Box>
                <h1>My App</h1>
                <p>Welcome to my app!</p>
            </Box>
            <TableContainer>
                    <Table size='lg'>
                        <Thead>
                            <Tr>
                                <Th>ID</Th>
                                <Th>Content</Th>
                            </Tr>
                        </Thead>
                        <Tbody>
                            {openaiMessage.map((message) => (
                                <Tr key={message.id}>
                                    <Td>{message.id}</Td>
                                    <Td>{message.content[0].text.value}</Td>
                                </Tr>
                            ))}
                        </Tbody>
                    </Table>
                </TableContainer>
            

        </Container>

    
    );
};

export default MainPage;