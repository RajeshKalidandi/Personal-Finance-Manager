import shutil
import os
from datetime import datetime

class BackupService:
    def __init__(self, db_path, backup_dir):
        self.db_path = db_path
        self.backup_dir = backup_dir

    def create_backup(self):
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"backup_{timestamp}.db"
        backup_path = os.path.join(self.backup_dir, backup_file)
        
        shutil.copy2(self.db_path, backup_path)
        return backup_path

    def restore_backup(self, backup_file):
        backup_path = os.path.join(self.backup_dir, backup_file)
        if not os.path.exists(backup_path):
            raise FileNotFoundError(f"Backup file {backup_file} not found")
        
        shutil.copy2(backup_path, self.db_path)