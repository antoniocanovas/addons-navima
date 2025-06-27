from odoo import models


class DocumentsDocument(models.Model):
    _inherit = "documents.document"

    def documents_project_task_autoassign(self):
        project = False
        for record in self:
            # Skip folders to avoid errors
            if record.type == "folder":
                continue

            if record.res_model == "project.project":
                project = self.env["project.project"].search(
                    [("id", "=", record.res_id)]
                )
            if record.res_model == "project.task":
                project = (
                    self.env["project.task"]
                    .search([("id", "=", record.res_id)])
                    .project_id
                )

            if project.id:
                for task in project.task_ids:
                    tasklen = len(task.name)
                    if record.name[:tasklen].lower() == task.name.lower():
                        record.write({"res_model": "project.task", "res_id": task.id})
                        if (
                            not task.displayed_image_id.id
                            and "image" in record.mimetype
                        ):
                            task.write({"displayed_image_id": record.attachment_id.id})
