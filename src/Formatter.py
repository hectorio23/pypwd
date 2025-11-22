import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class ExporterStrategy(ABC):
    @abstractmethod
    def export(self, content: dict, filename: str):
        pass


class JsonExporter(ExporterStrategy):
    def export(self, content: dict, filename: str):
        with open(filename, "w") as f:
            json.dump(content, f, indent=4)
        print(f"[+] Exported to {filename} (JSON)")


class TxtExporter(ExporterStrategy):
    def export(self, content: dict, filename: str):
        with open(filename, "w") as f:
            for i, (key, value) in enumerate(content.items(), 1):
                f.write(f"[{i}] {key.ljust(12)} ->     {value}\n")
        print(f"[+] Exported to {filename} (TXT)")


class XmlExporter:
    def export(self, content: dict, filename: str):
        root = ET.Element("passwords")
        for key, value in content.items():
            entry = ET.SubElement(root, "entry")
            k = ET.SubElement(entry, "key")
            k.text = key
            v = ET.SubElement(entry, "value")
            v.text = str(value)

        self.indent(root)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        print(f"[+] Exported to {filename} (XML)")

    def indent(self, elem, level=0):
        indent_str = "\n" + ("  " * level)
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = indent_str + "  "
            for child in elem:
                self.indent(child, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = indent_str
        else:
            if not elem.tail or not elem.tail.strip():
                elem.tail = indent_str


class YamlExporter(ExporterStrategy):
    def export(self, content: dict, filename: str):
        with open(filename, "w") as f:
            for key, value in content.items():
                f.write(f"{key}: {value}\n")
        print(f"[+] Exported to {filename} (YAML sintetic)")


class PasswordExporter:
    def __init__(self, strategy: ExporterStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ExporterStrategy):
        self.strategy = strategy

    def export(self, content: dict, filename: str):
        self.strategy.export(content, filename)

