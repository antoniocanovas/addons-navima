{
    "name": "Document → Auto-assign Project Task",
    "version": "18.0.1.0.0",
    "category": "Documentos",
    "website": "https://www.puntsistemes.es",
    "author": "Punt Sistemes",
    "summary": "Clasifica automáticamente los documentos de un proyecto en sus tareas,"
    "en función de que el principio del nombre coincida con el de alguna de las tareas."
    "Si es tipo imagen pondrá dicha imagen como portada de la tarea,"
    " en caso de que este campo no esté asignado.",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "documents",
        "project",
        "documents_project",
    ],
    "data": [
        "data/automation_docs.xml",
    ],
}
