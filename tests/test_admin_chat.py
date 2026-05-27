# SPDX-License-Identifier: Apache-2.0
"""Tests for built-in admin chat UI behavior."""

from pathlib import Path


CHAT_TEMPLATE = (
    Path(__file__).parent.parent / "omlx" / "admin" / "templates" / "chat.html"
)


class TestChatModelAliasHandling:
    """Built-in chat should handle display ids from /v1/models."""

    def test_model_type_map_includes_display_ids_for_vision_gate(self):
        """Aliased VLMs should still show image upload controls in chat."""
        template = CHAT_TEMPLATE.read_text()

        assert "syncDisplayModelMetadata(displayModels)" in template
        assert "this.modelTypeMap[displayModel.id] = statusModel.model_type || 'llm';" in template
        assert "this.modelDisplayIdMap[statusModel.id] = displayModel.id;" in template

    def test_default_model_is_resolved_to_display_id(self):
        """The chat default model can be canonical while /v1/models uses aliases."""
        template = CHAT_TEMPLATE.read_text()

        assert "resolveDisplayModelId(modelId)" in template
        assert "const defaultDisplayModel = defaultModel ? this.resolveDisplayModelId(defaultModel) : null;" in template
        assert "this.currentModel = defaultDisplayModel;" in template
