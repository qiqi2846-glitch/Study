import os
import json
import unittest

class TestCrawlComments(unittest.TestCase):
    def setUp(self):
        """Thiết lập đường dẫn file cần kiểm thử"""
        self.file_path = "data/cmts.json"

    def test_file_exists(self):
        """Kiểm tra file có tồn tại không"""
        print("🔍 Đang kiểm tra file:", os.path.abspath(self.file_path))
        self.assertTrue(os.path.exists(self.file_path), "❌ File cmts.json không tồn tại!")

    def test_valid_json_format(self):
        """Kiểm tra file có đúng định dạng JSON không"""
        print("🔍 Đang kiểm tra file:", os.path.abspath(self.file_path))
        with open(self.file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                self.fail("❌ File cmts.json không phải định dạng JSON hợp lệ!")

    def test_non_empty_data(self):
        """Kiểm tra file có ít nhất một bình luận"""
        print("🔍 Đang kiểm tra file:", os.path.abspath(self.file_path))
        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertGreater(len(data), 0, "❌ Không có bình luận nào được crawl!")

    def test_valid_comment_structure(self):
        """Kiểm tra mỗi bình luận có đủ thông tin user và comment"""
        print("🔍 Đang kiểm tra file:", os.path.abspath(self.file_path))
        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            self.assertIn("user", item, "❌ Thiếu trường 'user' trong dữ liệu!")
            self.assertIn("comment", item, "❌ Thiếu trường 'comment' trong dữ liệu!")

if __name__ == "__main__":
    unittest.main()
