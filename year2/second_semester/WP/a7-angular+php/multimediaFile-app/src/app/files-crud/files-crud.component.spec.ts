import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FilesCrudComponent } from './files-crud.component';

describe('FilesCrudComponent', () => {
  let component: FilesCrudComponent;
  let fixture: ComponentFixture<FilesCrudComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [FilesCrudComponent]
    });
    fixture = TestBed.createComponent(FilesCrudComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
