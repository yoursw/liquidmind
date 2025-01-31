from django import forms
from django.utils.safestring import mark_safe

class DurationPickerWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        hours = list(range(24))  # Hours from 0 to 23
        minutes = list(range(0, 60, 15))  # Minutes in increments of 15
        _widgets = (
            forms.Select(attrs=attrs, choices=[(hour, hour) for hour in hours]),
            forms.Select(attrs=attrs, choices=[(minute, minute) for minute in minutes]),
        )
        super().__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            # Logic to decompress the duration value into hours and minutes
            # (You'll need to implement this based on how you store the duration)
            return [value.seconds // 3600, (value.seconds // 60) % 60]
        return [None, None]

    def value_from_datadict(self, data, files, name):
        hours, minutes = data.get(name + '_0'), data.get(name + '_1')
        if hours and minutes:
            # Logic to combine hours and minutes into a duration value
            # (You'll need to implement this)
            return datetime.timedelta(hours=int(hours), minutes=int(minutes))
        return None

    def render(self, name, value, attrs=None, renderer=None):
        hours_widget, minutes_widget = self.widgets  # Unpack widgets for clarity

        # Create individual components with clear structure
        duration_toggle = f"""
            <div class="duration-toggle">
                <input type="checkbox" name="duration_tracked" id="id_duration_tracked">
                <label for="id_duration_tracked">Track Duration</label>
            </div>
        """

        duration_fields = f"""
        <div class="duration-fields hidden">
            <label for="id_hours">Hours:</label>
            {hours_widget.render(name + '_0', value, attrs=attrs)}
            <label for="id_minutes">Minutes:</label>
            {minutes_widget.render(name + '_1', value, attrs=attrs)}
        </div>
        """

        # Combine components into the final output
        output = f"""
            <div class="duration-picker">
                {duration_toggle}
                {duration_fields}
            </div>
        """
        return mark_safe(output)
