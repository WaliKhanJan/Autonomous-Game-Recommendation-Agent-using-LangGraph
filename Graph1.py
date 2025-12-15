from typing_extensions import TypedDict

class State(TypedDict):
    graph_info: str


### Initializing the 3 nodes
def start_play(state:State):
    print("Start node has been called")
    return {"graph_info":state["graph_info"] + "I am planning to play"}


def Table_Tennis(state:State):
    print("TT node has been called")
    return {"graph_info":state["graph_info"] + "Table_Tennis"}


def Cricket(state:State):
    print("Cricket node has been called")
    return {"graph_info":state["graph_info"] + "Cricket"}

### Decision Logic
import random
from typing import Literal   ###Literal is basically the constant

def Decision(state:State)->Literal['Table_Tennis','Cricket']:
    if random.random()>0.5:
        return "Table_Tennis"
    else:
        return "Cricket"

### Constructing the Graph

from IPython.display import Image,display
from langgraph.graph import StateGraph,START,END

###Building the Graph
graph=StateGraph(State)

### adding all the nodes
graph.add_node("start_play",start_play)
graph.add_node("Table_Tennis",Table_Tennis)
graph.add_node("Cricket",Cricket)

###Connecting the nodes
graph.add_edge(START,"start_play")
graph.add_conditional_edges("start_play",Decision)
graph.add_edge("Table_Tennis",END)
graph.add_edge("Cricket",END)

###Compiling the Graph
graph_builder=graph.compile()

### To view the graph
png_bytes = graph_builder.get_graph().draw_mermaid_png()

with open("langgraph.png", "wb") as f:
    f.write(png_bytes)

print("Graph saved as langgraph.png")
