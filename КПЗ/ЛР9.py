import graphviz
from graphviz import Digraph
import subprocess
from typing import Optional


class DiagramGenerator:
    """Base class for generating different types of diagrams."""
    
    def __init__(self, diagram_name: str, comment: str = ''):
        """Initialize the diagram with basic settings."""
        self.diagram = Digraph(comment=comment)
        self.diagram_name = diagram_name
        self.format = 'png'
        
    def add_nodes(self, nodes: dict) -> None:
        """Add multiple nodes to the diagram."""
        for node_id, node_label in nodes.items():
            self.diagram.node(node_id, node_label)
    
    def add_edges(self, edges: list) -> None:
        """Add multiple edges to the diagram."""
        for source, target, label in edges:
            self.diagram.edge(source, target, label)
    
    def render_and_open(self, view: bool = False) -> Optional[str]:
        """Render the diagram and optionally open it in VSCode."""
        try:
            path = self.diagram.render(
                self.diagram_name,
                format=self.format,
                view=view,
                cleanup=True
            )
            self._open_in_vscode(path)
            return path
        except Exception as e:
            print(f"Error generating diagram: {str(e)}")
            return None
    
    @staticmethod
    def _open_in_vscode(filepath: str) -> None:
        """Open the generated file in VSCode."""
        try:
            subprocess.run(['code', filepath], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to open in VSCode: {str(e)}")


class InteractionDiagram(DiagramGenerator):
    """Generates interaction diagrams for trading systems."""
    
    def __init__(self):
        super().__init__('interaction_diagram', 'Trading System Interaction Diagram')
        
    def create_diagram(self) -> None:
        """Create the complete interaction diagram."""
        nodes = {
            'T': 'Trader',
            'TS': 'Trading System',
            'O': 'Order',
            'SE': 'Stock Exchange',
            'M': 'Module'
        }
        
        edges = [
            ('T', 'TS', 'ЗапитПозики (сума, умови)'),
            ('TS', 'O', 'СтворитиБорг (сума, відсотки)'),
            ('O', 'SE', 'РезервуватиКошти()'),
            ('SE', 'T', 'НадатиПозиченіКошти()'),
            ('T', 'M', 'ПовернутиБорг (сума, відсотки)'),
            ('M', 'SE', 'ЗакритиБорг()'),
            ('SE', 'O', 'ОновитиСтатусБоргу()')
        ]
        
        self.add_nodes(nodes)
        self.add_edges(edges)


class CollaborationDiagram(DiagramGenerator):
    """Generates collaboration diagrams for trading systems."""
    
    def __init__(self):
        super().__init__('collaboration_diagram', 'Trading System Collaboration Diagram')
        
    def create_diagram(self) -> None:
        """Create the complete collaboration diagram."""
        nodes = {
            'T': 'Trader',
            'TS': 'Trading System',
            'O': 'Order',
            'SE': 'Stock Exchange',
            'M': 'Module'
        }
        
        edges = [
            ('T', 'TS', 'ЗапитПозики (сума, умови)'),
            ('TS', 'O', 'СтворитиБорг (сума, відсотки)'),
            ('O', 'SE', 'РезервуватиКошти()'),
            ('SE', 'T', 'НадатиПозиченіКошти()'),
            ('T', 'M', 'ПовернутиБорг (сума, відсотки)'),
            ('M', 'SE', 'ЗакритиБорг()'),
            ('SE', 'O', 'ОновитиСтатусБоргу()')
        ]
        
        self.add_nodes(nodes)
        self.add_edges(edges)


def main():
    """Main function to generate and display diagrams."""
    try:
        interaction_diagram = InteractionDiagram()
        interaction_diagram.create_diagram()
        interaction_diagram.render_and_open()
        
        collaboration_diagram = CollaborationDiagram()
        collaboration_diagram.create_diagram()
        collaboration_diagram.render_and_open()
        
    except Exception as e:
        print(f"Error in diagram generation: {str(e)}")


if __name__ == "__main__":
    main()