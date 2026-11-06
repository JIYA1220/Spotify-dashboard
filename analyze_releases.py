"""Reproduce the release-pattern numbers quoted in README.md from spotify-2023.csv."""
import pandas as pd

df = pd.read_csv("spotify-2023.csv", encoding="latin-1")
df["streams"] = pd.to_numeric(df["streams"], errors="coerce")
df["release_date"] = pd.to_datetime(
    dict(year=df.released_year, month=df.released_month, day=df.released_day)
)
df["weekday"] = df.release_date.dt.day_name()
df["quarter"] = df.release_date.dt.quarter

print(f"Tracks: {len(df)} (streams missing for {df.streams.isna().sum()})")
print(f"Release years: {df.released_year.min()} to {df.released_year.max()}")

fri = (df.weekday == "Friday").sum()
print(f"\nFriday releases: {fri} of {len(df)} = {fri / len(df):.1%}")
print("Share of total streams from Friday releases: "
      f"{df.loc[df.weekday == 'Friday', 'streams'].sum() / df.streams.sum():.1%}")
print("\nReleases by weekday:")
print(df.weekday.value_counts().to_string())

print("\nReleases by quarter (share):")
print((df.quarter.value_counts(normalize=True).sort_index() * 100).round(1).to_string())

print("\nReleases by month:")
print(df.released_month.value_counts().sort_index().to_string())

top = df.nlargest(int(len(df) * 0.10), "streams")
print(f"\nTop 10% of tracks ({len(top)}) hold {top.streams.sum() / df.streams.sum():.1%} of streams")
