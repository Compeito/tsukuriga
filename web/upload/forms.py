from django import forms
from django.forms import inlineformset_factory

from browse.models import Label, VideoProfileLabelRelation
from .models import UploadedPureVideo, VideoProfile


class VideoFileUploadForm(forms.ModelForm):
    file = forms.FileField(
        label='動画ファイル', widget=forms.FileInput(),
        help_text='mp4,avi,gif,movの動画ファイル、100MBまで'
    )

    class Meta:
        model = UploadedPureVideo
        fields = ('file',)


class VideoProfileForm(forms.ModelForm):
    description = forms.CharField(
        label='動画説明', widget=forms.Textarea(), required=False,
        help_text='URLと@, #から始まる文字列はそれぞれリンク、ユーザーページへのリンク、ハッシュタグに置換されます'
    )
    ordered_fps = forms.IntegerField(
        label='コマ送り機能用fps値の指定', min_value=1, required=False,
        help_text="""アップロードしたファイルと異なるfpsでコマ送り機能を使いたい場合に入力して下さい。<br>
動画ファイル自体のfpsは変わりません。指定がない場合は動画ファイルから読み取った値を使用します"""
    )
    allows_anonymous_comment = forms.BooleanField(
        label='匿名のコメントを許可する', required=False,
        help_text='拒否設定にした時点で追加されていたコメントは全て匿名設定がオフになります'
    )
    release_type = forms.ChoiceField(
        label='公開状態', choices=VideoProfile.RELEASE_TYPES[:-1],
        help_text='限定公開は新着順など一部ページに表示されなくなります'
    )

    class Meta:
        model = VideoProfile
        fields = ('title', 'description', 'file', 'ordered_fps', 'is_loop', 'allows_anonymous_comment', 'release_type')


class VideoProfileLabelRelationForm(forms.ModelForm):
    label = forms.ModelChoiceField(queryset=Label.objects.filter(is_active=True), required=False)

    class Meta:
        model = VideoProfileLabelRelation
        fields = ('label',)


LabelInlineFormSet = inlineformset_factory(
    parent_model=VideoProfile,
    model=VideoProfileLabelRelation,
    form=VideoProfileLabelRelationForm,
    extra=3, max_num=3, can_delete=False
)


class VideoImportForm(forms.Form):
    url = forms.URLField(label='URL', widget=forms.URLInput(attrs={'placeholder': 'https://...'}))
