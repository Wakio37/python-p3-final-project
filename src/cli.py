import click
from playlist import Playlist

playlist = Playlist()

@click.group()
def main():
    pass

@main.command()
@click.argument('title')
def add_track(title):
    playlist.add_track(title)
    click.echo(f'Track "{title}" added to the playlist.')

@main.command()
@click.argument('title')
def remove_track(title):
    playlist.remove_track(title)
    click.echo(f'Track "{title}" removed from the playlist.')

@main.command()
def list_tracks():
    tracks = playlist.get_all_tracks()
    if not tracks:
        click.echo('The playlist is empty.')
    else:
        click.echo('Playlist tracks:')
        for track in tracks:
            click.echo(track)

if __name__ == '__main__':
    main()
