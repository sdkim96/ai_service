from pydantic import BaseModel, Field
from typing import List, Optional, Generic, TypeVar, Union, Dict, Any

class Prompt(BaseModel):
    gpt: str = None
    midjourney : str = None

    def which_prompt(self):
        if self.gpt is not None:
            return self.gpt
        elif self.midjourney is not None:
            return self.midjourney
        else:
            raise ValueError("No valid prompt provided")
        

class CreateMessageInput(BaseModel):
    role: str
    content: str
    thread_id : str
        

class BaseOpenaiEntity(BaseModel):
    id: str
    object: str
    created_at: int
    metadata: Dict[str, str] = Field(..., max_items=16, max_length_key=64, max_length_value=512)

class ToolResource(BaseModel):
    file_ids: Optional[List[str]] = None
    vector_store_ids: Optional[List[str]] = None

class CodeInterpreterResource(ToolResource):
    file_ids: Optional[List[str]] = Field(None, max_items=20)

class FileSearchResource(ToolResource):
    vector_store_ids: Optional[List[str]] = Field(None, max_items=1)

class ToolResources(BaseModel):
    code_interpreter: Optional[CodeInterpreterResource] = None
    file_search: Optional[FileSearchResource] = None

class Text(BaseModel):
    value: str
    annotations: List[Any] 

class TextContentBlock(BaseModel):
    type: str
    text: Text

class IncompleteDetails(BaseModel):
    reason: str
    incomplete_at: Optional[int] = None

class ImageFile(BaseModel):
    type: str = "image_file"
    image_file: str

class TextBlock(BaseModel):
    type: str = "text"
    text: str

class ContentItem(BaseModel):
    type: str
    text: Optional[Text] = None
    image_file: Optional[ImageFile] = None

class Attachment(BaseModel):
    file_id: str
    tools: List[str]

class LastError(BaseModel):
    code: str
    message: str

class IncompleteDetails(BaseModel):
    reason: str
    incomplete_at: Optional[int] = None

class ToolCall(BaseModel):
    # Define properties for tool calls if needed
    pass

class TruncationStrategy(BaseModel):
    type: str
    last_messages: Optional[int] = None


class Message(BaseOpenaiEntity):
    thread_id: str
    status: Optional[str] = None # Should be one of "in_progress", "incomplete", or "completed"
    incomplete_details: Optional[IncompleteDetails] = None
    completed_at: Optional[int] = None
    role: str  # Should be either "user" or "assistant"
    content: List[ContentItem]
    assistant_id: Optional[str] = None
    run_id: Optional[str] = None
    attachments: Optional[List[Attachment]] = None


class Thread(BaseOpenaiEntity):
    tool_resources: Optional[ToolResources] = None


class Assistant(BaseOpenaiEntity):
    name: Optional[str] = Field(None, max_length=256)
    description: Optional[str] = Field(None, max_length=512)
    model: str
    instructions: Optional[str] = Field(None, max_length=256000)
    tools: List[str] = Field(..., max_items=128)
    tool_resource: Optional[Dict[str, ToolResource]] = None
    temperature: Optional[float] = Field(None, ge=0, le=2)
    top_p: Optional[float] = Field(None, ge=0, le=1)
    response_format: Optional[Union[str, Dict[str, Any]]] = None


class Run(BaseOpenaiEntity):
    thread_id: str
    assistant_id: str
    status: Optional[str] = None
    required_action: Optional[Dict[str, Any]] = None
    last_error: Optional[LastError] = None
    expires_at: Optional[int] = None
    started_at: Optional[int] = None
    cancelled_at: Optional[int] = None
    failed_at: Optional[int] = None
    completed_at: Optional[int] = None
    incomplete_details: Optional[IncompleteDetails] = None
    model: Optional[str] = None
    instructions: Optional[str] = None
    tools: Optional[List[str]] = None
    tool_calls: Optional[List[ToolCall]] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    max_prompt_tokens: Optional[int] = None
    max_completion_tokens: Optional[int] = None
    truncation_strategy: Optional[TruncationStrategy] = None
    tool_choice: Optional[Union[str, Dict[str, Any]]] = None
    response_format: Optional[Union[str, Dict[str, Any]]] = None